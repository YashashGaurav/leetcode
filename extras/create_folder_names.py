from pathlib import Path


def runner(problem_title: str):
    '''
    TODO: add ability to add links and comments to the
    solution folder's sol file
    '''
    folder_name = ""

    for s in problem_title:
        if s.isalnum():
            folder_name += s
        if s == " ":
            folder_name += "_"

    p = Path(
        str(Path(__file__).parent.parent) + "/problems" + "/" + folder_name
    )
    p.mkdir(parents=True, exist_ok=True)
    
    exp_fn = 'experiments.py'
    exp_path = p / exp_fn
    with exp_path.open("w", encoding ="utf-8") as f:
        f.write(f"""'''
    {problem_title}
'''

""")


runner("question_title_here")
