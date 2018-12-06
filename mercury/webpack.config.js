const path = require('path');
//const HtmlWepbackPlugin = require('html-webpack-plugin');
//const CleanWebpackPlugin = require('clean-webpack-plugin');
const webpack = require('webpack');


module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        },
      },
      {
        test:  /\.css$/,
        use: {
          loader: "css-loader"
        },
      },
      {
        test: /\.svg$/,
        include: [path.join(__dirname, "./mercury/frontend/src/components/Images")],
        use: {
          loader: "url-loader"
        }
        //loaders:[
          //'babel-loader',
        //{
          //loader: 'svg-react-loader',
          //query: {
            //jsx: true
          //}
        //},
      //]
      },
      
    ],

  },
};