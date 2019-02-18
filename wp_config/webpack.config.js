var path = require('path')
var webpack = require('webpack')
var MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = env => {
  var config = JSON.parse(env)
  return {
    mode: "development",
    entry: config.entry,
    output: {
      path: path.join(__dirname, '..', 'app', 'static'),
      filename: '[name].bundle.js'
    },
    resolve: {
      extensions: ['.js', '.jsx', '.ts', '.tsx']
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx|ts|tsx)$/,
          exclude: /(node_modules)/,
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/env',
              '@babel/preset-react',
              '@babel/preset-typescript'
            ],
            plugins: [
              '@babel/plugin-proposal-class-properties'
            ]
          }
        },
        {
          test: /\.(sa|sc|c)ss$/,
          use: [
            {loader: MiniCssExtractPlugin.loader},
            {loader: 'css-loader'},
            {loader: 'sass-loader'}
          ]
        }
      ]
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: '[name].bundle.css'
      })
    ],
    devServer: {
      port: config.port,
      host: config.host,
      public: config.public_url,
      publicPath: '/static/',
      proxy: [{
        context: [config.proxy_context],
        target: config.target
      }]
    }
  }
}
