import logging
import random
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from config import (
    KEYWORDS, DEFAULT_SEARCH_COUNT, DRIVER_PATH, BROWSER_OPTIONS,
    SCROLL_DELAY_MIN, SCROLL_DELAY_MAX, SEARCH_DELAY_MIN, SEARCH_DELAY_MAX,
    INTER_SEARCH_DELAY_MIN, INTER_SEARCH_DELAY_MAX, WAIT_TIMEOUT
)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BingRewardsBot:
    """Microsoft Rewards Bing搜索自动化机器人"""

    def __init__(self):
        self.driver = None
        self._setup_driver()

    def _setup_driver(self):
        """设置Edge浏览器驱动"""
        try:
            # 设置浏览器选项
            options = webdriver.EdgeOptions()
            if BROWSER_OPTIONS.get("headless"):
                options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            # 初始化驱动程序
            try:
                service = Service(EdgeChromiumDriverManager().install())
                logger.info("成功下载Edge驱动程序")
            except Exception as e:
                logger.warning(f"自动下载驱动程序失败: {e}")
                logger.info(f"使用本地驱动程序: {DRIVER_PATH}")
                service = Service(DRIVER_PATH)

            self.driver = webdriver.Edge(service=service, options=options)
            logger.info("Edge浏览器初始化成功")

        except Exception as e:
            logger.error(f"驱动程序初始化失败: {e}")
            raise

    def simulate_human_scroll(self):
        """模拟人类的滚动行为"""
        try:
            page_height = self.driver.execute_script("return document.body.scrollHeight")
            scroll_times = random.randint(1, 4)
            current_position = 0

            for _ in range(scroll_times):
                scroll_distance = random.randint(100, 500)
                if random.random() < 0.3:
                    scroll_distance = -scroll_distance

                if 0 <= current_position + scroll_distance < page_height:
                    self.driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
                    current_position += scroll_distance
                else:
                    target = 0 if current_position + scroll_distance < 0 else page_height
                    self.driver.execute_script("window.scrollTo(0, arguments[0]);", target)
                    break

                time.sleep(random.uniform(SCROLL_DELAY_MIN, SCROLL_DELAY_MAX))

        except Exception as e:
            logger.error(f"滚动时发生错误: {e}")

    def bing_search(self, query):
        """执行Bing搜索"""
        try:
            self.driver.get("https://www.bing.com")
            search_box = WebDriverWait(self.driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.ID, "sb_form_q"))
            )
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)

            # 等待搜索结果加载
            WebDriverWait(self.driver, WAIT_TIMEOUT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h2 a"))
            )

            # 模拟滚动行为
            self.simulate_human_scroll()

            # 额外延迟
            time.sleep(random.uniform(SEARCH_DELAY_MIN, SEARCH_DELAY_MAX))

        except Exception as e:
            logger.error(f"搜索 '{query}' 时发生错误: {e}")

    def run(self, search_count=None):
        """运行搜索任务"""
        if search_count is None:
            search_count = DEFAULT_SEARCH_COUNT

        try:
            # 打开登录页面
            self.driver.get("https://login.live.com")
            logger.info("请手动登录Microsoft账户，然后按Enter继续...")
            input()

            # 执行搜索
            for i in range(search_count):
                keyword = random.choice(KEYWORDS)
                logger.info(f"执行第 {i + 1} 次搜索: {keyword}")
                self.bing_search(keyword)

                # 搜索间延迟
                if i < search_count - 1:
                    time.sleep(random.uniform(INTER_SEARCH_DELAY_MIN, INTER_SEARCH_DELAY_MAX))

            logger.info(f"已完成 {search_count} 次搜索！")

        except Exception as e:
            logger.error(f"运行过程中发生错误: {e}")
        finally:
            if self.driver:
                self.driver.quit()
                logger.info("浏览器已关闭")


def main():
    """主函数"""
    try:
        # 解析命令行参数
        search_count = int(sys.argv[1]) if len(sys.argv) > 1 else None

        # 创建机器人实例并运行
        bot = BingRewardsBot()
        bot.run(search_count)

    except KeyboardInterrupt:
        logger.info("用户中断执行")
    except Exception as e:
        logger.error(f"程序执行失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()