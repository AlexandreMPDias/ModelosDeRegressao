const { dependencies, ..._ } = require('./help')

const [a,b, ...args] = process.argv;

_.run(`pip install ${args.join(' ')}`).then(dependencies.update);