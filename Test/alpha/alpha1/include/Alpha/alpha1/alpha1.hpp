#pragma once

#ifdef _WIN32
  #define ALPHA1_EXPORT __declspec(dllexport)
#else
  #define ALPHA1_EXPORT
#endif

ALPHA1_EXPORT void  alpha1();