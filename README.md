
#note: the following code will work only on linux operating system (eg : rhel 8) 

# Automation-Using-Python


[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](http://forthebadge.com)   [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)      [![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)



we are using python to automate docker , Hadoop , AWS, Linux.The real motive behind the project is to make it useful for those who might not be that into the respective technologies but will be able to perform all the basic functions.


# Table of contents

- [Usage](#usage)
- [Demo](#demo)
- [Installation](#installation)
- [Recommended configurations](#recommended-configurations)
- [Custom configurations](#custom-configurations)
- [Updating](#updating)
- [Uninstallation](#uninstallation)
- [Contributing](#contributing)
- [Future Scope](#future-scope)

</br></br>

# Usage

[(Back to top)](#table-of-contents)

📌 Automates following tech-stacks: -  

👉 Docker

👉 Hadoop

👉 Linux

👉 AWS
</br>

# Demo
[(Back to top)](#table-of-contents)

📌 The first Screen.

![First_image_options](https://media-exp1.licdn.com/dms/image/C4D12AQHWNyU-nS04-g/article-inline_image-shrink_1000_1488/0/1604856609369?e=1637193600&v=beta&t=Rf-2c5Pa36J7Z0eQoRtfLUE6Ds938RLdFMx0YQlS7W4)

_______________________________________________________________________________________________________

👉 Here is a simple demo of the working model


![working_model(1)](https://media-exp1.licdn.com/dms/image/C4D12AQHnbB2PcadzDQ/article-inline_image-shrink_1000_1488/0/1604857503634?e=1637193600&v=beta&t=H_FGCjY-HSC7eI-cJnAZLBOIJ6xuefF99T9oPJyHWC0)

_______________________________________________________________________________________________________

📌 Option 7 helps in creating hadoop name node.

![Name_node](https://media-exp1.licdn.com/dms/image/C4D12AQF5LAp6Nz00KQ/article-inline_image-shrink_1000_1488/0/1604857833063?e=1637193600&v=beta&t=NXIJEI1_umpTJ25l11k8R09xkpaCA8KhEFGKjVB4Xt8)

_______________________________________________________________________________________________________


👉 Another Tech-Stack is Docker which is a containerization tool.

![Docker](https://media-exp1.licdn.com/dms/image/C4D12AQHVIzfGXBncNQ/article-inline_image-shrink_1000_1488/0/1604860605866?e=1637193600&v=beta&t=NfqQ2hyGs8rWJSMn8tuC3ueHSwCjoZpttPgq22T94hA)
_______________________________________________________________________________________________________

For more details 👉 [(click here)](http://confusedprogrammer.unaux.com/2021/09/14/automation-using-python/)




# Installation


[(Back to top)](#table-of-contents)

1. Install git (preferably, version >= 2.0) and python (preferably, version >=3.6)
 [(windows)](https://www.maketecheasier.com/install-git-bash-on-windows/)
 For Linux :
 ```bash
    sudo yum instal git -y
    sudo yum install python -y
 ```
 
2. Copy the github url from the repository : 

 ```bash
 https://github.com/SiddharthaShandilya/automation-using-python.git
 ```

3. Select a Directory in local system and use 

  ```bash 
  git clonehttps://github.com/SiddharthaShandilya/automation-using-python.git           
  ```

    *Note for `git clone command`  Please make sure that you have proper internet connection. *

    *Note for `python` Please try to anaconda for running the app.*  

4. Create a seperate virtual environment to avoid conflict between python libraries :
    ```bash
    python3 -m venv new-env 
    ```

5. Activate the virtual env: 👉 [(click Here)](https://www.programshelp.com/help/python/activate_virtual_environment_python_windows_10.html)
6. Install all the libraries as well as software for the application.Do download Docker, Hadoop, AWS.

6. Have a look at [Recommended configurations](#recommended-configurations) and [Custom configurations](#custom-configurations).


</br></br>


# Recommended configurations

[(Back to top)](#table-of-contents)

Download the following software: Docker
<!--

1. To add some short command (say, `lc`) with some flag options (say, `-l`, `-A`, `--sd`) by default, add this to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.) :
    ```sh
    alias lc='colorls -lA --sd'
    ```

2. For changing the icon(s) to other unicode icons of choice (select icons from [here](https://nerdfonts.com/)), change the YAML files in a text editor of your choice (say, `subl`)

    ```sh
    subl $(dirname $(gem which colorls))/yaml
    ```

</br></br>
-->

# Custom configurations

[(Back to top)](#table-of-contents)


you can overwrtite the existng codes and add new features. 

In order to add new features in the application you need to create a seperate file where you can store all the neccessary configuration code.
<!--
You can overwrite the existing icons and colors mapping by copying the yaml files from `$(dirname $(gem which colorls))/yaml` into `~/.config/colorls`, and changing them.

- To overwrite color mapping :

  Please have a look at the [list of supported color names](https://github.com/sickill/rainbow#color-list). You may also use a color hex code as long as it is quoted within the YAML file and prefaced with a `#` symbol.

  Let's say that you're using the dark color scheme and would like to change the color of untracked file (`??`) in the `--git-status` flag to yellow. Copy the defaut `dark_colors.yaml` and change it.

  ```sh
  cp $(dirname $(gem which colorls))/yaml/dark_colors.yaml ~/.config/colorls/dark_colors.yaml
  ```

  In the `~/.config/colorls/dark_colors.yaml` file, change the color set for `untracked` from `darkorange` to `yellow`, and save the change.

  ```
  untracked: yellow
  ```

  Or, using hex color codes:

  ```
  untracked: '#FFFF00'
  ```

- To overwrite icon mapping :

  Please have a look at the [list of supported icons](https://nerdfonts.com/). Let's say you want to add an icon for swift files. Copy the default `files.yaml` and change it.

  ```sh
  cp $(dirname $(gem which colorls))/yaml/files.yaml ~/.config/colorls/files.yaml`
  ```

  In the `~/.config/colorls/files.yaml` file, add a new icon / change an existing icon, and save the change.


  ```
  swift: "\uF179"
  ```

- User contributed alias configurations :

  - [@rjhilgefort](https://gist.github.com/rjhilgefort/51ea47dd91bcd90cd6d9b3b199188c16)

-->
</br></br>

# Updating

[(Back to top)](#table-of-contents)

Want to update to the latest version of `chat_app`?

<!--
```sh
gem update colorls
```
-->


</br></br>

# Uninstallation

[(Back to top)](#table-of-contents)

Want to uninstall and revert back to the old style? No issues (sob). Please feel free to open an issue regarding how we can enhance `chat_app`.

<!--
```sh
rmdir ./automation-using-python
```
-->

</br></br>

# Contributing

[(Back to top)](#table-of-contents)

Your contributions are always welcome! Please have a look at the [contribution guidelines](CONTRIBUTING.md) first. :tada:


</br>

# Future Scope
[(Back to top)](#table-of-contents)

Adding Voice chat app will make it more user friendly
Adding face recognition system will make it more secure.
Accessing all the file via Web-Browser will allow us to have more better UI.





