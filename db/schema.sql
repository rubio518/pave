create table webhooks(
	id uuid not null default gen_random_uuid(),
	client_id text null,
	url text null
);

insert into webhooks (client_id, url) values ('1234','https://webhook.site/728342da-1f00-4fb6-99ed-7552845e1103');