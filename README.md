# kuid

A universally unique identifier, is essentially a shorter version of 
a UUID and is commonly used to identify records in various applications.

## Rationale
When writing a web application, often times we would like to keep the URLs short.

```
http://localhost/posts/5eAU5M3OyqyuX93bJHopJV
```
This certainly gives a more concise look than the following.

```
http://localhost/posts/b9926647-86a7-4f31-9c38-f7cf711bf865
```

# Installation

kuid can be installed via pypi.

```
pip install kuid
```

# Usuage

The following section describes a basic usage of base62.

```
import uuid
import kuid

kuid.encode(uuid.UUID('b9926647-86a7-4f31-9c38-f7cf711bf865'))
'5eAU5M3OyqyuX93bJHopJV'

>>> kuid.decode('5eAU5M3OyqyuX93bJHopJV')
UUID('b9926647-86a7-4f31-9c38-f7cf711bf865')
```

# Credits
* https://dev.to/sonus21/kuid-compressed-universally-unique-identifier-384i
* https://github.com/suminb/base62