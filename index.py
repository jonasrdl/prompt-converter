import re

def zsh_to_bash_prompt(zsh_prompt):
    prompt_mappings = {
        '%n': r'\u',   
        '%m': r'\h',
        '%~': r'\w',
        '%/': r'\W',
        '%$': r'\$',
    }

    bash_prompt = re.sub(
        r'%[nms~/$]',
        lambda match: prompt_mappings.get(match.group(0), ''),
        zsh_prompt
    )
    return bash_prompt

zsh_prompt = input("Enter zsh prompt to convert: ")
bash_prompt = zsh_to_bash_prompt(zsh_prompt)
print(bash_prompt)
