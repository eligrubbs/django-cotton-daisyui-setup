# django-cotton-daisyui-setup

Bringing the power for daisyUI and django-cotton to your django repo, while forcing as little as possible onto your architecture.

## TLDR; What is this repo?

This repository manages a slim script to copy/paste an opinionated (in the best way) [django-cotton](https://django-cotton.com/) django app containing a component library into the directory of your choosing so you can hit the ground running building your design system on top of [daisyui](https://daisyui.com) in your django project.

It also has guides on how exactly to hook-up and tweak the files you just dumped into your repository.

## Who is this repo for?

- You have a Django project with a significant front-end portion.
- You have chosen DaisyUI as the basis for your design system.
- You don't mind using `django-cotton` to manage some of your components.

## Why copy/paste and not `pip install`?

I believe it makes sense that the developer own a copy of the code powering their design system.

I think the boundary of separation exists where it should right now, at the tailwind CSS level. If you need to make tweaks to the design system,
use the CSS files managing daisyUI. If you need to add, change, or remove certain components, well they exist right there for you to use.

One downside is if daisyUI releases new versions that extend or change the API, you are kind of required then to manually adjust the specific component cotton templates that  

## Goals of this repo

- The setup should take less than 2 minutes
- The effects of using this repo should be easily reversible
- Try as much as possible to NOT force design / architecture decisions when using this repo
    - don't tell you what icons to use, what js/css build pipeline you need to use, etc.

