from .utils import str_to_date_tuple, tuple_to_datestring, last_day_of_month
from argparse import ArgumentParser
from datetime import date

def arg_handler():
    # Tool information
    parser = ArgumentParser(prog="PyGressionTester",description= "A pythonic regression test tool")

    parser.add_argument('--from', '-f', action='store', dest='fromDate', required=True)
    parser.add_argument('--to', '-t', action='store', dest='toDate', required=False)

    return parser.parse_args()

def get_args(args: ArgumentParser):

    tmp = args.fromDate
    result = str_to_date_tuple(tmp)
    if result[0] == -1:
        (day, month, year) = result
        result = (1, month, year)
        fromDate = tuple_to_datestring(result)
        toDate = str(last_day_of_month(date(year, month, 1)))
    else:
        fromDate = tuple_to_datestring(result)
        if args.toDate is not None:
            toDate = str_to_date_tuple(args.toDate)
        else:
            toDate = fromDate

    return (fromDate, toDate)