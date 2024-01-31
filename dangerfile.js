import { message, danger, fail, warn } from "danger";

const modifiedMD = danger.git.modified_files.join("- ");
message("Changed Files in this PR: \n - " + modifiedMD);

// Function to check the commit message format according to Conventional Commits
function checkCommitMessageFormat(commit) {
	const lines = commit.message
		.split("\n")
		.filter((line) => line.trim() !== "");
	const title = lines[0];
	const description = lines.slice(1);

	// Regex to validate Conventional Commits format
	const ccRegex =
		/^(feat|fix|docs|style|refactor|test|chore|perf)(\(\w+\))?:\s.{1,50}$/;

	// Check 1: Validate Conventional Commit format and title length
	if (!ccRegex.test(title)) {
		fail(
			`Commit title does not follow Conventional Commits format or exceeds 50 characters: "${title}"`
		);
	}

	// Check 2: Empty line between title and description (if description exists)
	// if (description.length > 0 && description[0].trim() !== "") {
	// 	fail("No empty line between commit title and description.");
	// }

	// Check 3: Description has at least 5 characters
	if (description.length > 1 && description[1].trim().length < 5) {
		fail("Commit description is less than 5 characters.");
	}

	// Check 4: Each line in the description does not have more than 72 characters
	description.forEach((line, index) => {
		if (line.length > 72) {
			fail(
				`Line ${
					index + 1
				} in commit description exceeds 72 characters: "${line.substring(
					0,
					69
				)}..."`
			);
		}
	});
}

// Iterate over each commit to check the message format
danger.git.commits.forEach(checkCommitMessageFormat);
