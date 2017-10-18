const webpack = require('webpack');
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const extractStyles = new ExtractTextPlugin('[name]');

module.exports = {
  context: path.resolve(__dirname, 'src/js'),
  entry: {
    'app.bundle.js': './app.js',
    'style.css': '../css/style.css',
    'grid.css': '../css/grid.css',
    'dropdown.js': './dropdown.js'
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
    filename: '[name]'
  },
  resolve: {
    modules: [path.resolve(__dirname, 'src'), 'node_modules']
  },
  plugins: [
    extractStyles
  ]
};
