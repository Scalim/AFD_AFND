module.exports = {
    lintOnSave: false,
    publicPath: process.env.NODE_ENV == "production" ? "/app-teoria-de-grafos/" : "/",
    transpileDependencies: ["buefy"]
  };