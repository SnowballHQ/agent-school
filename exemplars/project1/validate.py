"""A tiny schema checker: just the parts schema.json uses. Returns a list of problems (empty = valid)."""
import re


def check(value, schema, path="answer"):
    problems = []
    allowed = schema.get("type")
    if allowed is not None:
        allowed = allowed if isinstance(allowed, list) else [allowed]
        names = {"string": str, "boolean": bool, "object": dict, "null": type(None)}
        if not any(isinstance(value, names[t]) for t in allowed):
            return ["%s should be %s, got %r" % (path, " or ".join(allowed), value)]
    if "enum" in schema and value not in schema["enum"]:
        problems.append("%s must be one of %s, got %r" % (path, schema["enum"], value))
    if "pattern" in schema and isinstance(value, str) and not re.search(schema["pattern"], value):
        problems.append("%s=%r does not match %s" % (path, value, schema["pattern"]))
    if isinstance(value, dict):
        for name in schema.get("required", []):
            if name not in value:
                problems.append("%s is missing" % name)
        for name, sub in schema.get("properties", {}).items():
            if name in value:
                problems += check(value[name], sub, name)
        if schema.get("additionalProperties") is False:
            for name in value:
                if name not in schema.get("properties", {}):
                    problems.append("%s is not an allowed field" % name)
    return problems
