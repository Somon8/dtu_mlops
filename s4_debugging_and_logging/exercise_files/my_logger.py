import sys
from loguru import logger

logger.remove()  # Remove the default logger
logger.add(sys.stdout, level="WARNING")  # Add a new logger with WARNING level
logger.add("my_log.log", rotation="100 MB")

logger.debug("Used for debugging your code.")
logger.info("Informative messages from your code.")
logger.warning("Everything works but there is something to be aware of.")
logger.error("There's been a mistake with the process.")
logger.critical("There is something terribly wrong and process may terminate.")

@logger.catch
def f(x):
     100 / x
def g():
    f(10)
    f(0)

g()