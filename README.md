# Mercury Camera Configurator

The Mercury Configurator is a web application designed to disambiguate the complicated process of figuring out how to 
configure the multitude of different possible camera builds. This application is designed to take the user through each step of 
the configuration process and help them choose a camera that will work and makes sense for their needs. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

What things you need to run the project

* [Python 3](https://www.python.org/)
* [PIP](https://pypi.org/project/pip/) - Python Package manager. It should just come with your Python3 Installation
* [NodeJS](https://nodejs.org/en/) - Mainly just to make use of NPM 
* [Django](https://www.djangoproject.com/) 
* [React](https://reactjs.org/)
* [Webpack](https://webpack.js.org/)


### Running the App
Once you have the project downloaded, run it using this Python Command

```
python manage.py runserver
```

The app will no be veiwable on port 8000 on your local machine. 

### Dependencies and Packages 

Taken from package.json file


```
    "babel-core": "^6.26.3",
    "babel-loader": "^7.1.5",
    "babel-plugin-transform-class-properties": "^6.24.1",
    "babel-preset-env": "^1.7.0",
    "babel-preset-react": "^6.24.1",
    "file-loader": "^2.0.0",
    "prop-types": "^15.6.2",
    "react": "^16.4.2",
    "react-dom": "^16.4.2",
    "reactstrap": "^6.3.1",
    "url-loader": "^1.1.1",
    "weak-key": "^1.0.1",
    "webpack": "^4.16.5",
    "webpack-cli": "^3.1.0"y 
```

```
    "bootstrap": "^4.1.2",
    "braintree-web": "^2.32.1",
    "css-loader": "^1.0.0",
    "style-loader": "^0.22.1",
    "svg-loader": "0.0.2",
    "svg-react-loader": "^0.4.5"

```

## Core Feature still needed

> Deployment - Needs system in place in order to deploy a production version of the application

> System Lens - The system lens configuration system still needs to be built 

> Purchasing/store functionality - users needs to be able to purchase their configurations

## Other Issues and Bugs

> Some scaling issues with svgs (especially the larger svgs such as the System Lens)

> Drop down controls affect each other in left column

> Need to limit information on records returned from database in the lens stack section 


## Possible Future Features 

> Login system to save configurations

> Fully fleshed out forum attached to the configurator (or Mercury instagram)

> Create Default Bundles available to purchase as base configurations

> Have Mercury warehouse catalog, where any part available can be purchased with needing to be a part of a config (for advanced users)



## Authors

* **Connor Lovejoy** (cml120@pitt.edu) 



## License

No Current License 

## Acknowledgments

* Thanks to Biddle's Escape for the coffee
* And Jay and Tom for the company
* And to Zach for the project and Mercury
