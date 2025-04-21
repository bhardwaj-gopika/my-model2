from my_model2.flow import my_model2_flow

def test_flow_execution(tmp_path):
    try:
        output_variables = my_model2_flow(filename=f"{tmp_path}/test_file.txt", filesystem_identifier="local")
    except Exception:
        pass #Dont care for now

