const fs = require('fs');
const path = require('path');
const child_process = require('child_process');

function getDependencies() {
	const location = "./dependencies.json"

	const load = () => {
		return JSON.parse(fs.readFileSync(location, { encoding: 'utf-8'}));
	}

	const save = (content) => {
		console.log('Saving update on dependencies');
		fs.writeFileSync(location, JSON.stringify(content, undefined, "\t"), {encoding: 'utf-8'});
	}

	const update = () => {
		console.log(`Updating dependencies registry`)
		run('pip freeze',{}, true).then(out => {
			const entries = out.split('\n')
				.filter(a => a.match('=='))
				.map(line => line.replace('\r', ''))
				.map(line => line.split('=='));
			const deps = {}
			entries.forEach(([packageName, version]) => {
				deps[packageName] = version;
			})

			console.log(deps);
			save(deps);
		})
	}

	return {
		get content() {
			return load();
		},
		set content(data) {
			save(data);
		},
		update
	}
}

const dependencies = getDependencies();

function run(cmd ,options = {}, hideOut = false) {
	const [base, ...rest] = cmd.split(' ');
	return new Promise((resolve, reject) => {
		const output = [];
		const proc = child_process.spawn(base,rest, { encoding: 'utf-8', ...options });
		proc.stdout.setEncoding('utf8');
		proc.stdout.on('data', (data) => {
			if(!hideOut) {
				console.log(data);

			}
			output.push(data);
		})
		proc.stdout.on('throw', () => reject())
		proc.stdout.on('end', () => resolve(output.join('')))
	})
}

module.exports = {
	fs,
	path,
	dependencies,
	run,
	freeze: () => {
		return run('pip freeze',{}, true);
	}
}