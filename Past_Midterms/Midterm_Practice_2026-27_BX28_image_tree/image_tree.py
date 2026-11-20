"""CSE202 mock midterm -- binary image compression. Complete Q1--Q5."""

def uniform_block(image, row, col, size):
    """Q1: return 0 or 1 if the block is uniform, else None."""
    raise NotImplementedError


def encode(image):
    """Q2: build the canonical quadtree of a nonempty square image."""
    raise NotImplementedError


def pixel(tree, size, row, col):
    """Q3: obtain a pixel without reconstructing the image."""
    raise NotImplementedError


def black_pixels(tree, size):
    """Q4: count 1-pixels without reconstructing the image."""
    raise NotImplementedError


def decode(tree, size):
    """Q5: reconstruct the image as a list of independent row lists."""
    raise NotImplementedError

# Q3: Explain briefly why the search visits at most log2(size) internal nodes.
# TODO
