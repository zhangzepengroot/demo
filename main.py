import logging

import dy


if __name__ == '__main__':
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    url = input('请输入直播间链接:')
    dy.parseLiveRoomUrl(url)
