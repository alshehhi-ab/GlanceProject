
# sana.py
# Sana is a class that represents an entire gregorian calendar year
# Sana is Arabic for year, from proto-semitic šan-at (meaning year). Used instead of "year" to avoid confusion.

from datetime import datetime, date, time
import youm


class Sana:

    def __init__(self, year_in):
        self.year_id = str(year_in)
        self._start_ord = date(year_in, 1, 1).toordinal()
        self._end_ord = date(year_in, 12, 31).toordinal()
        self._num_days = self._end_ord - self._start_ord + 1

        # Hash Table for Youms
        self.youms = {str(date.fromordinal(n)): youm.Youm(date.fromordinal(n))
                      for n in range(self._start_ord, self._end_ord+1)}

        # ordinal represents the day number since Jan 1, 1 (day 1)
        # using the range of ordinals of a year, we can generate a dictionary for all the days of the year,
        # accounting for leap years as well.
        # Each entry in the dict represents a default youm object.


    def get_youm(self, date_in):
        """ Finds and returns a Youm object in Sana
        :param date_in: date object, is input date used for search
        :return: found Youm object
        """
        # Check if date is in Sana

        # This error would typically be bypassed by an appropriate filter in an interface file.
        if date.toordinal(date_in) not in range(self._start_ord, self._end_ord + 1):
            raise ValueError("Error: Date not in Range of file.")

        return self.youms[str(date_in)]

    def update_youm(self, date_in, youm_in):
        """ Updates value stored for a certain youm, helpful for when tasks or events are modified
        :param date_in: date object input, is the date representation of the youm to be updated
        :param youm_in: new youm data to be inserted and updated
        :return: None
        """

        # Check if date is in Sana

        # This error would typically be bypassed by an appropriate filter in an interface file.
        if date.toordinal(date_in) not in range(self._start_ord, self._end_ord+1):
            raise ValueError("Error: Date not in Range of file.")

        key = str(date_in)

        # Update dictionary entry
        self.youms[key] = youm_in

