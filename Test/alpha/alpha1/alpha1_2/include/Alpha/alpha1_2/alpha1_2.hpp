#pragma once

#ifdef _WIN32
  #define ALPHA1_2_EXPORT __declspec(dllexport)
#else
  #define ALPHA1_2_EXPORT
#endif

ALPHA1_2_EXPORT void alpha1_2();