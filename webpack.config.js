const webpack = require('webpack');
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const extractStyles = new ExtractTextPlugin('style.css');

module.exports = {
  context: path.resolve(__dirname, 'src/js'),
  entry: {
    app: './app.js'
  },
  module: {
    loaders: [
      {
        test: /\.css/,
        use: extractStyles.extract({
          use: [
            {
              loader: 'css-loader',
              options: { importLoaders: 1 }
            },
            'postcss-loader'
          ]
        })
      }
    ]
  },
  output: {
    path: path.resolve(__dirname, 'jcms/static/jcms'),
    filename: '[name].bundle.js'
  },
  resolve: {
    modules: [path.resolve(__dirname, 'src'), 'node_modules']
  },
  plugins: [
    extractStyles
  ]
};