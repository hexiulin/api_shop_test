import logging
import os


def get_logger():
    # 获取记录器
    logger = logging.getLogger("api_test")

    if not logger.handlers:  #防止重复添加
        # 设置门槛
        logger.setLevel(logging.INFO)

        # 创建输出渠道
        console_handler = logging.StreamHandler()  # 控制台

        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")  # 文件（自动创建 logs 文件夹）
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        file_handler = logging.FileHandler(os.path.join(log_dir, "test.log"), mode="a", encoding="utf-8")

        # 创建格式器
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s')

        # 给渠道绑定格式
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        #  组装
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

# 实例化供外部使用
logger = get_logger()