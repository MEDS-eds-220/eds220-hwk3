OK_FORMAT = True

test = {   'name': 'q5d',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q3(student_data):\n'
                                               '...     try:\n'
                                               "...         expected_data = pd.read_csv('data/q5d_df.csv').drop(columns='Unnamed: 0')\n"
                                               '...         pd.testing.assert_frame_equal(expected_data, student_data)\n'
                                               '...     except AssertionError:\n'
                                               "...         raise AssertionError('Incorrect answer.')\n"
                                               '>>> test_q3(spills_per_county)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
