const { dependencies, ..._ } = require('./help')

const dps = dependencies.content;

const cmd = Object.entries(dps).reduce((out, [ packageName, version ]) => {
	return `${out} ${packageName}==${version}`;
}, 'pip install')

_.run(cmd).then(dependencies.update)