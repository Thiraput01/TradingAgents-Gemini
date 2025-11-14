│ /root/miniconda3/envs/tradingagents/lib/python3.13/site-packages/google/ai/generativelanguage*v1beta/services/generative_service/t │
│ ransports/base.py:105 in **init** │
│ │
│ 102 │ │ │ │ credentials_file, \*\*scopes_kwargs, quota_project_id=quota_project_id │
│ 103 │ │ │ ) │
│ 104 │ │ elif credentials is None and not self.\_ignore_credentials: │
│ ❱ 105 │ │ │ credentials, * = google.auth.default( │
│ 106 │ │ │ │ \*\*scopes_kwargs, quota_project_id=quota_project_id │
│ 107 │ │ │ ) │
│ 108 │ │ │ # Don't apply audience if the credentials file passed from user. │
│ │
│ ╭──────────────────────────────────────────────────────────── locals ────────────────────────────────────────────────────────────╮ │
│ │ always_use_jwt_access = True │ │
│ │ api_audience = None │ │
│ │ client_info = <google.api_core.gapic_v1.client_info.ClientInfo object at 0x76c13c8b55b0> │ │
│ │ credentials = None │ │
│ │ credentials_file = None │ │
│ │ host = 'generativelanguage.googleapis.com' │ │
│ │ kwargs = {} │ │
│ │ quota_project_id = None │ │
│ │ scopes = None │ │
│ │ scopes_kwargs = {'scopes': None, 'default_scopes': ()} │ │
│ │ self = <google.ai.generativelanguage_v1beta.services.generative_service.transports.grpc.GenerativeServiceGrp… │ │
│ │ object at 0x76c13cc6de80> │ │
│ ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
│ │
│ /root/miniconda3/envs/tradingagents/lib/python3.13/site-packages/google/auth/\_default.py:739 in default │
│ │
│ 736 │ │ │ │ ) │
│ 737 │ │ │ return credentials, effective_project_id │
│ 738 │ │
│ ❱ 739 │ raise exceptions.DefaultCredentialsError(\_CLOUD_SDK_MISSING_CREDENTIALS) │
│ 740 │
│ │
│ ╭───────────────────────────────────── locals ──────────────────────────────────────╮ │
│ │ checkers = ( │ │
│ │ │ <function default.<locals>.<lambda> at 0x76c13c83ae80>, │ │
│ │ │ <function default.<locals>.<lambda> at 0x76c13c8385e0>, │ │
│ │ │ <function \_get_gae_credentials at 0x76c16f43bce0>, │ │
│ │ │ <function default.<locals>.<lambda> at 0x76c13c83a840> │ │
│ │ ) │ │
│ │ credentials = None │ │
│ │ default_scopes = () │ │
│ │ explicit_project_id = None │ │
│ │ project_id = None │ │
│ │ quota_project_id = None │ │
│ │ request = None │ │
│ │ scopes = None │ │
│ ╰───────────────────────────────────────────────────────────────────────────────────╯ │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
DefaultCredentialsError: Your default credentials were not found. To set up Application Default Credentials, see
https://cloud.google.com/docs/authentication/external/set-up-adc for more information.
