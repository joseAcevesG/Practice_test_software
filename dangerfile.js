import { message, danger, fail, warn } from "danger";

const modifiedMD = danger.git.modified_files.join("- ");
message("Changed Files in this PR: \n - " + modifiedMD);

// Function to check the commit message format
function checkCommitMessageFormat(commit) {
	const lines = commit.message
		.split("\n")
		.filter((line) => line.trim() !== "");
	const title = lines[0];
	const description = lines.slice(1);

	// Check 1: Git commits have a title of maximum 50 characters
	if (title.length > 50) {
		fail(
			`Commit title exceeds 50 characters: "${title.substring(0, 47)}..."`
		);
	}

	// Check 2 & 3: Empty line between title and description, and description has at least 5 characters
	if (description.length > 0) {
		if (description[0].trim() === "") {
			// Assuming there's an empty line, check if the next line (actual description) has at least 5 characters
			if (description.length > 1 && description[1].trim().length < 5) {
				fail("Commit description is less than 5 characters.");
			}
		} else {
			fail("No empty line between commit title and description.");
		}
	}

	// Check 4: Each line in the description does not have more than 72 characters
	description.forEach((line, index) => {
		if (line.length > 72) {
			// prettier-ignore
			fail(`Line ${index + 1} in commit description exceeds 72 characters: "${line.substring(0,69)}..."`);
		}
	});
}

// Iterate over each commit to check the message format
danger.git.commits.forEach(checkCommitMessageFormat);
