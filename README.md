# tboi-clone
This is a project to encourage learning programming with Python through game development. It's no loner an Isaac clone, but the name will stay until I fork it or something.

Pygame documentation: https://www.pygame.org/docs/  
Alternate documentation that isn't high contrast: https://devdocs.io/pygame/

## Pygame Examples
This library has a lot of great examples to pull ideas from: https://github.com/pygame/pygame/tree/main/examples

To run the `chimp.py` file:
```shell
python -m pygame.examples.chimp
```

## Prerequisites
* Python ~> 3.10

## Running the Game
Clone this repository (or download the zip):
```shell
git clone https://github.com/angelichorsey/tboi-clone.git
cd tboi-clone/
```

Setup your virtual environment and install modules:
```shell
python -m venv venv
.\venv\scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the game:
```shell
python run.py
```

<details>
  <summary>
  All commands if you want to just copy and paste all at once.
  </summary>

  ```shell
  git clone https://github.com/angelichorsey/tboi-clone.git
  cd tboi-clone/
  python -m venv venv
  .\venv\scripts\Activate.ps1
  python -m pip install -r requirements.txt
  python run.py
  ```
</details>

## Developing
There are no specific processes/policies for how to contribute. However, this is a learning project so this section contains references for programming newcomers.

At a minimum, you will need to install Python. It's also incredibly helpful to have an IDE (integrated development environment) with features that make writing Python easier. I have a detailed guide covering this:

[Setup Development Environment](https://github.com/angelichorsey/tips-n-tricks/tree/master/setup)

## Contributing
Playing around with the project doesn't require Git, but it is needed to actually push any changes back to this repo. It's not included yet in the guide above. After following that guide you should have Chocolatey installed which makes adding Git easy.

Open your terminal as administrator and run:
```shell
choco install git -y
```

Then all you need to do is normal Git operations like add, commit, and push. I'll make a separate page for that in my `tips-n-tricks` repo at some point.

## TODO Game Features
I've written out some of the many possible features a clone of Isaac should implement. They have estimated programming difficuly and a short specification of how to implement.

[Features to Implement](TODO.md)
