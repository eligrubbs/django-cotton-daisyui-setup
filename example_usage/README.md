# Example Project Usage

This repository contains an example of a tiny django project that uses the design system.

All it does is manage a django project, and a css / js pipeline, and show the demo of all the components

I have decided to call this sample web app `finklebob` as a way to unambiguiously identify this project instead of just using `example` everywhere. It also kind of my way of expressing how company names are becoming cartoonish and nonsensical (tubi, weebly, kaggle, zynga).


## Usage

You can look at this project easily by just running `uv sync && python manage.py runserver` when this directory is your current working directory.

## Setup / Opinions in this repo

1. CSS / JS is managed via vite.
    - The result of the build pipeline is a single app.css file. Should be pretty simple to gut this if this differs from your pipeline.
    - Not familiar with this setup? It's easy to start! Go set up [nvm](https://github.com/nvm-sh/nvm) to manage your node version, then come back and run `npm install`
