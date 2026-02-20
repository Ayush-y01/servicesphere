local jwt = require "resty.jwt"
local auth_header = ngx.var.http_Authorization

if not auth_header then
    ngx.status = 401
    ngx.say("Missing Authorization header")
    ngx.exit(401)
end

local _, _, token = string.find(auth_header, "Bearer%s+(.+)")

if not token then
    ngx.status = 401
    ngx.say("Invalid Authorization format")
    ngx.exit(401)
end

local jwt_obj = jwt:verify("supersecretkey", token)

if not jwt_obj.verified then
    ngx.status = 401
    ngx.say("Invalid token")
    ngx.exit(401)
end


--pass user info to service -- 
ngx.req.set_header("X-User-Id", jwt_obj.payload.sub)
ngx.req.set_header("X-User-Id", jwt_obj.payload.role)