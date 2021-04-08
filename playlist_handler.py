import httplib2
import os
import sys
import pprint

from oauth2_authentication import get_authenticated_service
from apiclient.errors import HttpError
# from oauth2client.tools import argparser

# args = argparser.parse_args()
service = get_authenticated_service()

# Build a resource based on a list of properties given as key-value pairs.
# Leave properties with empty values out of the inserted resource.
def build_resource(properties):
  resource = {}
  for p in properties:
    # Given a key like "snippet.title", split into "snippet" and "title", where
    # "snippet" will be an object and "title" will be a property in that object.
    prop_array = p.split('.')
    ref = resource
    for pa in range(0, len(prop_array)):
      is_array = False
      key = prop_array[pa]
      # Convert a name like "snippet.tags[]" to snippet.tags, but handle
      # the value as an array.
      if key[-2:] == '[]':
        key = key[0:len(key)-2:]
        is_array = True
      if pa == (len(prop_array) - 1):
        # Leave properties without values out of inserted resource.
        if properties[p]:
          if is_array:
            ref[key] = properties[p].split(',')
          else:
            ref[key] = properties[p]
      elif key not in ref:
        # For example, the property is "snippet.title", but the resource does
        # not yet have a "snippet" object. Create the snippet object here.
        # Setting "ref = ref[key]" means that in the next time through the
        # "for pa in range ..." loop, we will be setting a property in the
        # resource's "snippet" object.
        ref[key] = {}
        ref = ref[key]
      else:
        # For example, the property is "snippet.description", and the resource
        # already has a "snippet" object.
        ref = ref[key]
  return resource

# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs

# Create a playlist
def playlists_insert(properties, **kwargs):
  resource = build_resource(properties) # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs) # See full sample for function
  results = service.playlists().insert(
    body=resource,
    **kwargs
  ).execute()

  # pprint.pprint (results)
  return results

# Update a playlist 
def playlists_update(properties, **kwargs):
  resource = build_resource(properties) # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs) # See full sample for function
  results = service.playlists().update(
    body=resource,
    **kwargs
  ).execute()

  pprint.pprint(results)

# add a video to a playlist
def playlist_items_insert(properties, **kwargs):
  resource = build_resource(properties) # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs) # See full sample for function
  results = service.playlistItems().insert(
    body=resource,
    **kwargs
  ).execute()

  # pprint.pprint(results)
