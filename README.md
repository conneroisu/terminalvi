

# TerminalVi

Dataset labeling and viewing for machine learning engineers for use in headless environments. Utilizes terminal multiplexer to efficiently show videos and allow gradings, ratings, deletion flags, and more. 

View and Filter Huge Datasets in the terminal

To DO:

- [x]  selection system
- [x]  deletion-mark system
- [ ]  timed sequences(16s) transcript tool


## Modal

### Filter

## Features/keys

- “j” - Next Video
- “k” - Prev. Video
- “dd” - Mark file for deletion
- “ud” - Unmark file for deletion
- 

Command to enact:

```bash
$    terminalvi new-session -s terminalvi
$    python3 start.py

```

## libtmux notes

[libtmux/window.py at v0.13.0 · tmux-python/libtmux](https://github.com/tmux-python/libtmux/blob/v0.13.0/libtmux/window.py#L123-L160)

```bash

display_message(cmd: str, get_text: Literal[True])[source]
$ tmux display-message to the pane.

Displays a message in target-client status line.
```

```bash
resize_pane(*args: Any, **kwargs: Any)[source]
$ tmux resize-pane of pane and return self.

PARAMETERS:
target_pane (str) – target_pane, or -U,``-D``, -L, -R.

height (int) – resize-pane -y dimensions

width (int) – resize-pane -x dimensions
```

# Dependencies

## Tmux

- [https://github.com/tmux/tmux/wiki](https://github.com/tmux/tmux/wiki)

## Python
