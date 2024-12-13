<p align="center">

<h1 align="center"><img src="logo.png" width="30px" alt="Icon" title="Icon">.fsl Parser</h1>

<p align="center">
<img src="https://img.shields.io/badge/license-MIT-green" alt="License" title="License" >
<img src="https://img.shields.io/badge/license-Apache-blue" alt="License" title="License" >
</p>

</p>

> FluidServer Configuration Parser

You do not need this unless you are working with FluidServer. This is a parser for .fsl files, the configuration files used for FluidServer

FluidServer is a scalable POS-system server for - well - people who don't hate themselves. It makes it easier for system administrators and developer to use and implement - it's also more scalable than most POS-system servers.

<!--
# Installation
## Windows

Go to `fs.biitle.nl` and click on <button style="background-color: #19b4fe; border: 0px solid black; border-radius: 3px; padding: 3px 6px; color: white;">Download FluidServer</button>.

Open the installer and follow the steps, after that, you can run FluidServer.

## Linux (and Mac)
Run `curl fs.biitle.nl/install.sh | bash` to install FluidServer, follow the steps and run FluidServer from where you installed it to.

## Installerless
Clone the git repo by typing `git clone https://github.com/fgclue/fluidserver` and run the `make install`. Run `python api.py` to run FluidServer.
-->

# Usage Example

Import `fsl` and do `fsl.parse(yourfilehere.read())`. Make sure `yourfilehere` is a file with read permissions.

# Integration
Just follow the usage example, there is no reason for this section to be here.

# Meta
Built by clue <<lost@biitle.nl>>.

Distributed under the MIT license.

# Contributing
1. Fork the repo (https://github.com/FluidServer/fsl)
2. Create your feature branch (`git checkout -b feature/yournewfeature`)
3. Commit your changes (`git commit -am 'Add some change'`)
4. Push to the branch (`git push origin feature/yournewfeature`)
5. Create a new pull request

`SPDX-License-Identifier: MIT or Apache-2.0`