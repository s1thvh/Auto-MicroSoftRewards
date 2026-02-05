import os

# 关键词列表（100个，风格偏日常搜索场景）
KEYWORDS = [
    # 购物相关
    "Best laptops 2025", "Smartphone deals", "Fashion trends women", "Online shopping discounts",
    "Gaming console prices", "Home appliance reviews", "Sneaker brands", "Luxury watches",
    "Budget headphones", "Furniture sales", "Electronics deals", "Black Friday 2025",
    "Amazon best sellers", "Tech gadgets 2025", "Winter clothing trends", "Jewelry gift ideas",

    # 旅游与生活
    "Top travel destinations", "Cheap flights 2025", "Hotel booking tips", "Beach vacation ideas",
    "City break Europe", "Adventure travel packages", "Cruise deals 2025", "Travel insurance comparison",
    "Camping gear reviews", "Best hiking trails", "Family vacation spots", "Solo travel tips",
    "Backpacking destinations", "Luxury resorts Asia", "Travel safety tips", "Road trip ideas",

    # 新闻与时事
    "Breaking news today", "World news updates", "US election 2025", "Global economy trends",
    "Climate change solutions", "Political debates 2025", "International conflicts", "Tech industry updates",
    "Stock market predictions", "Health policy news", "Space mission updates", "Energy crisis 2025",

    # 学术与教育
    "Online courses free", "Best coding bootcamps", "Study abroad programs", "Scholarship opportunities",
    "Academic research tools", "Math learning apps", "History documentaries", "Science podcasts",
    "University rankings 2025", "Career training programs", "Language learning tips", "STEM resources",

    # 健康与健身
    "Weight loss diets", "Home workout routines", "Mental health tips", "Meditation apps",
    "Healthy meal plans", "Fitness equipment reviews", "Yoga for beginners", "Nutrition supplements",
    "Running shoes reviews", "Stress management techniques", "Sleep improvement tips", "Vegan recipes easy",

    # 娱乐与文化
    "New movie releases", "TV show reviews 2025", "Music festivals 2025", "Book recommendations",
    "Streaming service deals", "Celebrity news today", "Top video games 2025", "Art exhibitions",
    "Theater shows 2025", "Pop music charts", "Comedy specials Netflix", "Cultural events near me",

    # 科技与创新
    "Smart home devices 2025", "Wearable tech reviews", "Electric car prices", "AI innovations",
    "5G network updates", "Virtual reality headsets", "Drone technology", "Cybersecurity tips",
    "Tech startups 2025", "Cloud storage comparison", "Programming tutorials", "Data privacy laws",

    # 其他日常搜索
    "Local weather forecast", "Event planning ideas", "DIY craft projects", "Pet adoption near me",
    "Gardening for beginners", "Car maintenance tips", "Home renovation ideas", "Wedding planning guide",
    "Photography gear reviews", "Best coffee machines", "Restaurant reviews near me", "Online grocery delivery",
    "Real estate trends 2025", "Job search websites", "Personal finance apps", "Charity organizations"
]

# 默认搜索次数
DEFAULT_SEARCH_COUNT = 33

# 驱动程序路径
DRIVER_PATH = os.path.join("channel", "msedgedriver.exe")

# 浏览器选项
BROWSER_OPTIONS = {
    "headless": False,  # 设置为True启用无头模式
    "disable_gpu": True,
    "no_sandbox": True,
    "disable_dev_shm_usage": True
}

# 延迟设置（秒）
SCROLL_DELAY_MIN = 0.5
SCROLL_DELAY_MAX = 2.0
SEARCH_DELAY_MIN = 2.0
SEARCH_DELAY_MAX = 6.0
INTER_SEARCH_DELAY_MIN = 5.0
INTER_SEARCH_DELAY_MAX = 15.0

# 超时设置（秒）
WAIT_TIMEOUT = 10