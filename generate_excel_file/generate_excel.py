import data_mining.accessing_mobile_bg

def test_list_function(test_list):
    results = data_mining.accessing_mobile_bg.get_results_from_detailed_pages(test_list)
    return results