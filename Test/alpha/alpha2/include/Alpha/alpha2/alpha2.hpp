#pragma once

#ifdef _WIN32
  #define ALPHA2_EXPORT __declspec(dllexport)
#else
  #define ALPHA2_EXPORT
#endif

ALPHA2_EXPORT void alpha2();