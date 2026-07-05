# import logging as log
# log.basicConfig(filename="logFile.txt",level=log.DEBUG)
# log.debug("This indicates the debug information")
# log.info("This indicates the important information")
# log.error("This indicates the error information")
# log.warning("This indicates the warning information")
# log.critical("This indicates the critical information")

# print("all logs executed in logFile.txt")


import logging as log
log.basicConfig(filename="arithmatic.txt",level = log.DEBUG)
try:
    a  = int(input('Enter value of A :'))
    b  = int(input('Enter value of b :'))
    print(a/b)
    
except (ValueError,ZeroDivisionError) as msg:
    print(msg)
    log.exception(msg)

print("check arithmatic.txt for log details")