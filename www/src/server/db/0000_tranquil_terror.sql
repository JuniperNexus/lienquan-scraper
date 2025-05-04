-- Current sql file was generated after introspecting the database
-- If you want to run this migration please uncomment this code before executing migrations
/*
CREATE TABLE `heroes` (
	`id` integer PRIMARY KEY,
	`name` text,
	`image_url` text
);
--> statement-breakpoint
CREATE TABLE `skins` (
	`id` integer PRIMARY KEY,
	`hero_id` integer,
	`skin_image_url` text,
	FOREIGN KEY (`hero_id`) REFERENCES `heroes`(`id`) ON UPDATE no action ON DELETE cascade
);

*/