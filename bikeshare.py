import time
import pandas as pd
import numpy as np
# add abbreviations to the dictionary
CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv',
             'chi': 'chicago.csv', 'ny': 'new_york_city.csv', 'wa': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('=' * 70)
    print('\n**********Welcome to Bikeshare**********\nThank you for using Bikeshare!\n'
          'Let\'s explore some US Bikeshare data!''\n          ********************')
    print('=' * 70)

    # TO DO: get user input for city. HINT: Use a while loop to handle invalid inputs
    city = input('\nTo view the available bikeshare data, please select City from below:\n'
                 ' *Chicago\n *New York City\n *Washington\n\n ').lower()
    print('=' * 70)
    # validate city input
    while city not in CITY_DATA:
        print('\nOOPS!, Please enter a valid input\n')
        print('=' * 70)
    # rewrite the question
        city = input('\nTo view the available bikeshare data, please select City from below:\n'
                     ' *Chicago\n *New York City\n *Washington\n\n ').lower()
        print('=' * 70)

    # TO DO: get user input for month (all, january, february, ... , june). add a list for accepting abbreviations.
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    months_abb = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']

    month = input('\nIn Order to Filter {}\'s data reference to particular month or all months for not filtering '
                  'please select month from below:\n*January \n*February \n*March \n*April \n'
                  '*May \n*June \n*All\n\n'.format(city)).lower()
    print('=' * 70)

    while (month not in months) and (month not in months_abb):
        print('\nOOPS!, Please enter a valid input\n')
        print('=' * 70)
    # rewrite the question
        month = input('\nIn Order to Filter {}\'s data reference to particular month or all months for not filtering '
                      'please select month from below:\n*January \n*February \n*March \n*April \n'
                      '*May \n*June \n*All\n\n'.format(city)).lower()
        print('=' * 70)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) accepting abbreviations as well.
    days = ['sat', 'saturday', 'sun', 'sunday', 'mon', 'monday', 'tues', 'tuesday', 'wed', 'wednesday', 'thur',
            'thursday', 'fri', 'friday', 'all']
    day = input('\nIn Order to Filter {}\'s data in {} month(S) in a prticular day or even all days, '
                'please select a day from below:\n*Saturday \n*Sunday \n*Monday \n*Tuesday \n*Wednesday \n'
                '*Thursday \n*Friday \n*All\n\n'.format(city, month)).lower()
    print('=' * 70)

    while day not in days:
        print('\nOOPS!, Please enter a valid input\n')
        print('=' * 70)
        # rewrite the question
        day = input('\nIn Order to Filter {}\'s data in {} month(S) in a prticular day or even all days, '
                    'please select a day from below:\n*Saturday \n*Sunday \n*Monday \n*Tuesday \n*Wednesday \n'
                    '*Thursday \n*Friday \n*All\n\n'.format(city, month)).lower()
        print('=' * 70)

    print('='*70)
    print("\n*******Thank you....***** \n\n-You have selected\n {} City \n\n-You need the data of \n {} month(s) \n\n"
          "-And you have specified \n {} Weekday(S) to retrieve its data\n"
          "*******************\n".format(city.title(), month.title(), day.title()))
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # create dataframe from assigned city csv file
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # adding hour column
    df['Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        months_abbr = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        if month in months:
            month = months.index(month) + 1
            df = df[df['Month'] == month]
        # adding the index of month abbreviation month name to abbreviations
        elif month in months_abbr:
            month = months_abbr.index(month) + 1
            df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # add compare lists to accept full day name or abbreviations
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        days_abbr = ['sat', 'sun', 'mon', 'tues', 'wed', 'thur', 'fri']
        if day in days:
            df = df[df['Day of Week'] == day.title()]

        # Refelecting full day name to abbreviations
        elif day in days_abbr:
            day_abbr_index = days_abbr.index(day)
            day = days[day_abbr_index]
            df = df[df['Day of Week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # adding Months list
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    common_month_index = df['Month'].mode()[0]
    common_month = months[common_month_index-1]
    print('\nMost Common Month is:\n', common_month)

    # TO DO: display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    print('\nMost Common Day of the Week is:\n', common_day)

    # TO DO: display the most common start hour
    common_start_hour = df['Hour'].mode()[0]
    print('\nMost Common Hour (24 Format) is:\n', common_start_hour)

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('='*70)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe Most commonly used Start Station:\n ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe Most commonly used End Station: \n', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # adding Start Station and End Station Combination colomn to the dataframe.
    df['Trip stations'] = 'From: '+df['Start Station']+' --To: '+df['End Station']

    frequent_station_combination = df['Trip stations'].mode()[0]
    print('\nThe Most frequent combination of Start Station and End Station trip: \n', frequent_station_combination)

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('='*70)


def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('The total Travel Time in {} City in {} month(s) on {} '
          'Weekday(s) is:\n'.format(city, month, day), total_travel_time)
    # print('\nThe total Travel Time is:\n', total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('\nThe mean Travel Time in {} City in {} month(s) on {} '
          'Weekday(s) is:\n'.format(city, month, day), average_travel_time)

    # print('\nThe mean Travel Time is:\n',average_travel_time)
    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('='*70)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe User Type Counts as below:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # As data is not available for Gender at Washington, revert a message to user.
    if 'Gender' not in df:
        print('\nSorry,Gender User data in Washington is not available at the moment\n')
    else:
        print('\nThe Gender Counts as below:\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    # As data is not available for Birth Year at Washington, revert a message to user.
    if 'Gender' not in df:
        print('\nSorry,Birth Year data in Washington is not available at the moment\n')
    else:
        print('\nThe Earliest Year of Birth:\n', df['Birth Year'].min())
        print('\nThe Most Recent Year of Birth:\n', df['Birth Year'].max())
        print('\nThe Most Common Year of Birth:\n', df['Birth Year'].mode())
        print('\nThe Most Recent and Most Common Year of Birth:\n', df['Birth Year'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))


def raw_data_display(city, df):

    """This Function to give the option for user to display data of the selected City and display 5 in row each time"""
    print('\nWould you like to view Raw Data of Bikeshare in {} city?\n'.format(city))
    begin_row = 0
    while True:
        print('=' * 70)
        show = input('\nin order to display 5 Rows the available data in {} City, please type: '
                     'Yes/y for showing data or No/N to skip\n'.format(city)).lower()

        if show not in ['yes', 'y', 'no', 'n']:
            print('=' * 70)
            print('\nOOPS!, Please enter a valid input\n')
            print('=' * 70)
        elif show in ['no', 'n']:
            print('=' * 70)
            print('\n**********That\'s it. Thanks for using Bikeshare**********\n')
            print('=' * 70)
            break
        else:
            for show in ('yes', 'y'):
                print(df[begin_row:begin_row+5])
                begin_row = begin_row+5
                break


def main():
    while True:

        city, month, day = get_filters()
        print('=' * 70)
        df = load_data(city, month, day)
        print('=' * 70)
        time_stats(df)
        print('=' * 70)
        station_stats(df)
        print('=' * 70)
        trip_duration_stats(df, city, month, day)
        print('=' * 70)
        user_stats(df)
        print('=' * 120)
        print('\n**********Wish the above data meets your inquiries.**********\n')
        print('=' * 70)
        raw_data_display(city, df)
        # adding y as selection for yes
        restart = input('\nWould you like to restart? Enter yes/y for restart or enter any key to exit.\n')
        if (restart.lower() != 'yes') and (restart.lower() != 'y'):
            break


if __name__ == "__main__":
    main()
