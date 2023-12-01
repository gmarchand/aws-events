import click
import json
from tomark import Tomark

""" Create a cli to convert json to markdown table"""
@click.command()
@click.argument('file_path_json')
@click.argument('file_path_markdown', type=click.Path(exists=False))
def main(file_path_json,file_path_markdown ):
    """
    :param file_path: path to json file
    """
    # convert json file to dict

    with open(file_path_json, 'r') as f:
        data = json.load(f)
    # delete values
    for line in data:
        line.pop("sourceTitle")
        line.pop("sourceUrl")
        line.pop("time")
        line["title"] = f"[{line['title']}]({line['url']})".replace("|","-")
        line.pop("url")

    markdown = Tomark.table(data)
    # save text to file
    with open(file_path_markdown, 'w') as f:
        f.write(markdown)
if __name__ == '__main__':
    main()

