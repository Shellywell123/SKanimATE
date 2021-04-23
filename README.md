# SKanimATE

Python3 project that focuses on the simulation of flatground skateboard tricks, generated via rotatioal cartesian transformations in the form of animated gifs.

### Base N/Ollie Motion:

<p float="left">
  <img src="Images/gifs/Ollie.gif" width="400" />
  <img src="Images/gifs/Nollie.gif" width="400" />
</p>

### Tricks containing one rotational degree of freedom:

<p float="left">
  <img src="Images/gifs/Kickflip.gif" width="400" />
  <img src="Images/gifs/Nollie Kickflip.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/Heelflip.gif" width="400" />
  <img src="Images/gifs/Nollie Heelflip.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/BS 360 Pop Shuvit.gif" width="400" />
  <img src="Images/gifs/Nollie BS 360 Pop Shuvit.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/FS 360 Pop Shuvit.gif" width="400" />
  <img src="Images/gifs/Nollie FS 360 Pop Shuvit.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/Back Foot Impossible.gif" width="400" />
  <img src="Images/gifs/Nollie Back Foot Impossible.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/Front Foot Impossible.gif" width="400" />
  <img src="Images/gifs/Nollie Front Foot Impossible.gif" width="400" />
</p>

### Tricks containing two rotational degrees of freedom:

<p float="left">
  <img src="Images/gifs/Treflip.gif" width="400" />
  <img src="Images/gifs/Nollie Treflip.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/Lazerflip.gif" width="400" />
  <img src="Images/gifs/Nollie Lazerflip.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/Hardflip.gif" width="400" />
  <img src="Images/gifs/Nollie Hardflip.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/Inward Heelflip.gif" width="400" />
  <img src="Images/gifs/Nollie Inward Heelflip.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/Varial Kickflip.gif" width="400" />
  <img src="Images/gifs/Nollie Varial Kickflip.gif" width="400" />
</p>

<p float="left">
  <img src="Images/gifs/Varial Heelflip.gif" width="400" />
  <img src="Images/gifs/Nollie Varial Heelflip.gif" width="400" />
</p>

### Setup:
```bash
git clone https://github.com/Shellywell123/SKanimATE.git
```
```bash
python3 make_gifs.py
```
GIFs will appear in `Images/gifs/`
(Tricks orientations are all animated with respect to Regular stance)

### Features in continuous development:

 - skateboard component shapes
 - N/ollie motion
 - flip duration to catch time duration
 - rendering of model parts overlapping incorrectly, may move from matplotlib to mayavi
 - want to animate shoes to better illustrate stance
 - goofy/switch/fakie to be added
