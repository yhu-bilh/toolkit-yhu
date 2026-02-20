from nova_act import NovaAct

with NovaAct(starting_page="https://www.isharkfly.com") as nova:
    nova.act("Click categories")
    nova.act("Click discourse")
    nova.act("search for Discourse")
    nova.act("Click first result")