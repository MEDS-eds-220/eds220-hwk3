OK_FORMAT = True

test = {   'name': 'q5d',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q5d(student_data):\n'
                                               '...     try:\n'
                                               "...         expected_data = pd.read_csv('data/q5d_df.csv').drop(columns='Unnamed: 0')\n"
                                               '...         pd.testing.assert_index_equal(pd.RangeIndex(len(student_data)), student_data.index, exact=False)\n'
                                               "...         student_data = student_data.replace({'county': {'St. Lawrence': 'St Lawrence'}})\n"
                                               "...         expected_data = expected_data.sort_values('county').reset_index(drop=True)\n"
                                               "...         student_data = student_data.sort_values('county').reset_index(drop=True)\n"
                                               '...         pd.testing.assert_frame_equal(expected_data, student_data)\n'
                                               '...     except AssertionError:\n'
                                               "...         raise AssertionError('Incorrect answer.')\n"
                                               '>>> test_q5d(spills_per_county)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
