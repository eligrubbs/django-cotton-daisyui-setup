# Contributing to Design System

This guide outlines the process for adding a new component to the design system.

## Steps to Add a New Component

### 1. Identify the DaisyUI API
Scan the `.agents/skills/daisyui` repository to find the appropriate API and classes for your new component. This ensures that our components are consistent with the underlying library. Look for CSS classes (e.g., `input-primary`, `btn-sm`) and any JavaScript behavior required.

### 2. Create the Cotton Template
Create a new template folder for your component within `design_system/templates/cotton/ds/`. This is where the logic for the "Cotton" version of the component lives (using Django tags).

### 3. Create the Showcase Page
Create a showcase page for your component in `design_system/templates/showcase/components/`. This allows users to interact with and see all variations of the component.

### 4. Add Metadata
Register your new component in `design_system/intermal_data.py` by adding the relevant metadata (e.g., name, category, template path).

### 5. Update Progress
Finally, update the `PROGRESS.md` file to indicate that the new component has been successfully added to the design system.

---

## Detailed Example: Implementing the `Input` Component

Follow these steps to see how a component is implemented from start to finish.

### Step 1: Identify API
First, we look at DaisyUI's documentation (or the `daisyui` skill) and find that an input uses classes like `.input`, `.input-primary`, etc.

### Step 2: Create Cotton Template
Create `design_system/templates/cotton/ds/input/index.html`. We use `<c-vars>` to handle color and size variations via Django template tags.

```html
<c-vars
    class=""
    color=""
    size=""
    style_=""
    :colorClasses="{
        'neutral': 'input-neutral',
        'primary': 'input-primary',
        ...
    }"
    :sizeClasses="{
        'xs': 'input-xs',
        'sm': 'input-sm',
        ...
    }"
    validate
/>

<input
    class="input {{ colorClasses|get_item:color }} {{ sizeClasses|get_item:size }} {% if validate %}validator{% endif %} {{ class }}"
    {{ attrs }}
/>
```

### Step 3: Create Showcase Page
Create `design_system/templates/showcase/components/input.html`. This page renders various states of the input for demonstration.

```html
{% extends "showcase/_base.html" %}

{% block content %}
<div class="mb-8">
    <h2 class="text-3xl font-bold mb-2">Input</h2>
</div>

<section class="space-y-8">
    <div>
      <h3 class="text-lg font-semibold mb-4">Sizes</h3>
      <div class="flex flex-wrap gap-4">
          <c-ds.input size="sm" type="text" placeholder="Small"></c-ds.input>
          <c-ds.input size="lg" type="text" placeholder="Large"></c-ds.input>
      </div>
    </div>

    <div>
      <h3 class="text-lg font-semibold mb-4">Colors</h3>
      <div class="flex flex-wrap gap-4">
        <c-ds.input type="text" placeholder="Primary" class="input input-primary" />
        <c-ds.input type="text" placeholder="Success" class="input input-success" />
      </div>
    </div>
</section>
{% endblock %}
```

### Step 4: Add Metadata
In `design_system/intermal_data.py`, add the new component to the `COMPONENTS_METADATA` dictionary.

```python
    "input": ComponentInfo(
        name="Input",
        category=ComponentCategory.data_input,
        url_path_prefix="input",
        url_name="input",
        template_path_str=f"{TEMPLATE_COMMON_PREFIX}/input.html"
    ),
```

### Step 5: Update Progress
Update `PROGRESS.md` to mark the component as complete.
