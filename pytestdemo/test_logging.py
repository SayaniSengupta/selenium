# import logging
#
#
# def test_loggingDemo():
#     logger = logging.getLogger(__name__)
#     filehandler = logging.FileHandler("logfile.log")
#     formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
#     filehandler.setFormatter(formatter)
#     logger.addHandler(filehandler)
#
#     logger.setLevel(logging.DEBUG)
#     logger.debug("a debug statement is executed")
#     logger.info("information statement")
#     logger.warning("something went wrong")
#     logger.error("a major error has happend")
#     logger.critical("critical issue")
