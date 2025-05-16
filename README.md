# Dataiku Filter Listener

`DataikuFilterListener` is a Dash component library. The component listens for events triggered by Dataiku Dashboard Filters and gets filter values (available since Dataiku 13.0).

## Usage

* In your Dataiku instance, create a new Python code environment with the following requirements, or add them to an existing environment:
```
dash
dash_extensions
git+https://github.com/louisdorard/dataiku-filter-listener.git
```
* Create a new Dash webapp:
  * Paste code from [`usage.py`](usage.py).
  * Make sure to use the code env defined previously.
  * Start the webapp.
* Create a new Dashboard:
  * Define Filters.
  * Embed the Dash webapp.
* View the Dashboard and play with the Filters: the values you set should impact the webapp.

## Testing outside of Dataiku

It can be useful to test this component outside of Dataiku, for troubleshooting or debugging purposes.

* Start the Dash webapp
* Simulate events triggered by Dataiku Dashboard Filters:
  * Open the browser console.
  * Execute `window.postMessage({type: 'filters', filters: [{'name': 'titi'}]}, '*');`.
  * Confirm its impact on the Dash webapp. For instance, when running `usage.py`, we would expect to see the `filters` value set above, both in the webapp interface and in its logs.

### Starting the Dash webapp

GitHub Codespaces provides a quick way to set up a cloud environment to start Dash webapps:

* From this repository's home page, click on **Code** > **Codespaces** > **Create codespace on main**. The Codespace will be equipped with a Python environment built from [`requirements.txt`](requirements.txt), as specified in the Codespace configuration in [`.devcontainer/`](.devcontainer).
* Run `python usage.py` in the terminal (replace with the filename that contains your webapp's code, if different).
* When prompted by the Codespace, open the webapp in a new browser tab.

Alternatively, you can do this locally:

* Install the Python requirements listed in the [Usage](#usage) section.
* Clone this repository.
* Run `python usage.py` in the terminal.
* Open [http://localhost:8050](http://localhost:8050) in your web browser.

## What happens under the hood

The Dash component executes something similar to the following JavaScript code in order to listen to events of type ‘message’ and to get filter values from the event's data:

```js
window.addEventListener('message', function(event) {
  let filters = [];
    if (event.data && event.data.type && event.data.type === 'filters' && event.data.filters) {
        filters = event.data.filters;
        console.log(filters);
    }
});
```

Learn more about triggering and listening to message events:

* [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)
* [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)

## Why this component?

We want to catch events triggered by Dataiku Dashboard Filters and access filter values from Dash code. As explained in the Dataiku documentation (Dashboards » Insights reference » Webapp » [Accessing dashboard filters](https://doc.dataiku.com/dss/latest/dashboards/insights/webapp.html#accessing-dashboard-filters)), the Filters post events of type 'message' to the browser `window`. The message event's data contains a `type` property set to 'filters', and a `filters` property containing the actual filter values.

The popular [Dash Extensions](https://www.dash-extensions.com/) library contains an EventListener class but it can't be used because it doesn't listen to events at the window level (see [line 20](https://github.com/emilhe/dash-extensions/blob/57c350d861ed484c6210faefcf51d0ff99ee304d/src/lib/components/EventListener.react.js#L20): "if no children are provided, attach to the document object").

## How the component was built

```bash
cookiecutter gh:plotly/dash-component-boilerplate
cd dataiku_filter_listener/
npm install
npm run build
python usage.py
```

From the `dataiku_filter_listener/` directory:

* Added `dash-extensions-js` dependency to package.json
* Installed npm packages with `npm install`
* Wrote DataikuFilterListener.react.js by adapting Dash Extensions' [EventListener.react.js](https://github.com/emilhe/dash-extensions/blob/57c350d861ed484c6210faefcf51d0ff99ee304d/src/lib/components/EventListener.react.js#L8):
  * Simplified `getSource()`: this would always be the `window`.
  * Added code in `eventHandler()` to get the filter values from the message event.
* Built with `npm run build`

## Contributing

This section was automatically generated when creating the component.

See [CONTRIBUTING.md](./CONTRIBUTING.md)

### Install dependencies

If you have selected install_dependencies during the prompt, you can skip this part.

1. Install npm packages
    ```
    $ npm install
    ```
2. Create a virtual env and activate.
    ```
    $ virtualenv venv
    $ . venv/bin/activate
    ```
    _Note: venv\Scripts\activate for windows_

3. Install python packages required to build components.
    ```
    $ pip install -r requirements.txt
    ```
4. Install the python packages for testing (optional)
    ```
    $ pip install -r tests/requirements.txt
    ```

### Write your component code in `src/lib/components/DataikuFilterListener.react.js`.

- The demo app is in `src/demo` and you will import your example component code into your demo app.
- Test your code in a Python environment:
    1. Build your code
        ```
        $ npm run build
        ```
    2. Run and modify the `usage.py` sample dash app:
        ```
        $ python usage.py
        ```
- Write tests for your component.
    - A sample test is available in `tests/test_usage.py`, it will load `usage.py` and you can then automate interactions with selenium.
    - Run the tests with `$ pytest tests`.
    - The Dash team uses these types of integration tests extensively. Browse the Dash component code on GitHub for more examples of testing (e.g. https://github.com/plotly/dash-core-components)
- Add custom styles to your component by putting your custom CSS files into your distribution folder (`dataiku_filter_listener`).
    - Make sure that they are referenced in `MANIFEST.in` so that they get properly included when you're ready to publish your component.
    - Make sure the stylesheets are added to the `_css_dist` dict in `dataiku_filter_listener/__init__.py` so dash will serve them automatically when the component suite is requested.
- [Review your code](./review_checklist.md)

### Create a production build and publish:

1. Build your code:
    ```
    $ npm run build
    ```
2. Create a Python distribution
    ```
    $ python setup.py sdist bdist_wheel
    ```
    This will create source and wheel distribution in the generated the `dist/` folder.
    See [PyPA](https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-your-project)
    for more information.

3. Test your tarball by copying it into a new environment and installing it locally:
    ```
    $ pip install dataiku_filter_listener-0.0.1.tar.gz
    ```

4. If it works, then you can publish the component to NPM and PyPI:
    1. Publish on PyPI
        ```
        $ twine upload dist/*
        ```
    2. Cleanup the dist folder (optional)
        ```
        $ rm -rf dist
        ```
    3. Publish on NPM (Optional if chosen False in `publish_on_npm`)
        ```
        $ npm publish
        ```
        _Publishing your component to NPM will make the JavaScript bundles available on the unpkg CDN. By default, Dash serves the component library's CSS and JS locally, but if you choose to publish the package to NPM you can set `serve_locally` to `False` and you may see faster load times._

5. Share your component with the community! https://community.plotly.com/c/dash
    1. Publish this repository to GitHub
    2. Tag your GitHub repository with the plotly-dash tag so that it appears here: https://github.com/topics/plotly-dash
    3. Create a post in the Dash community forum: https://community.plotly.com/c/dash
