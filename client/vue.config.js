module.exports = {
  css: {
    loaderOptions: {
      scss: {
        additionalData: `@import "~@/assets/styles/variables.scss";`,
      },
    },
  },
  configureWebpack: {
    devtool: "source-map",
  },
  runtimeCompiler: true,
};
