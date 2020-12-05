module.exports = {
    module: {
        rules:[
            {
                test:/\.js$/,
                exclude:/node_modules/,
                use:{
                    loader:"babel-loader"
                }
            }
        ]
    },

    resolve: {
        fallback: {
          util: require.resolve("util/")
        }
    }
}