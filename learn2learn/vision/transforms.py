#!/usr/bin/env python3

"""

**Description**

A set of transformations commonly used in meta-learning vision tasks.
"""

import random
from torchvision import transforms


class RandomClassRotation(object):
    """

    [[Source]]()

    **Description**

    Samples rotations from a given list, uniformly at random.

    **Arguments**

    * **degrees** (list) - The rotations to be sampled.

    **Example**
    ~~~python
    transform = RandomClassRotation([0, 90, 180, 270])
    ~~~

    """

    def __init__(self, dataset, degrees):
        self.degrees = degrees
        self.dataset = dataset

    def __call__(self, task_description):
        rotations = {}
        for d in task_description:
            c = self.dataset.indices_to_labels[d[0]]
            if c not in rotations:
                rot = random.choice(self.degrees)
                rotations[c] = transforms.Compose([
                    transforms.ToPILImage(),
                    transforms.RandomRotation((rot, rot)),
                    transforms.ToTensor(),
                ])
            rotation = rotations[c]
            d[1].append(lambda x: (rotation(x[0]), x[1]))
        return task_description
