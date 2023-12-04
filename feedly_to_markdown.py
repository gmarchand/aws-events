import click
import json
from tomark import Tomark

# https://github.com/Barabazs/Feedly-Export-Save4Later/blob/main/SaveSavedEntries.js
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
    result = []
    for line in data:
        if line["url"].startswith("https://www.youtube.com"):
            line.pop("sourceTitle")
            line.pop("sourceUrl")
            line.pop("time")
            line["title"] = f"[{line['title']}]({line['url']})".replace("|","-")
            line.pop("url")
            result.append(line)

    print("number of entries:", len(result))
    markdown = Tomark.table(result)
    # save text to file
    with open(file_path_markdown, 'w') as f:
        f.write(markdown)
if __name__ == '__main__':
    main()

