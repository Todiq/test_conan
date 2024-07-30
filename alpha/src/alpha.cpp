#include <alpha/alpha.hpp>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <libxml/HTMLparser.h>

void traverse_dom_trees(xmlNode * a_node)
{
    xmlNode *cur_node = NULL;

    if(NULL == a_node)
    {
        //printf("Invalid argument a_node %p\n", a_node);
        return;
    }

    for (cur_node = a_node; cur_node; cur_node = cur_node->next) 
    {
        if (cur_node->type == XML_ELEMENT_NODE) 
        {
            /* Check for if current node should be exclude or not */
            printf("Node type: Text, name: %s\n", cur_node->name);
        }
        else if(cur_node->type == XML_TEXT_NODE)
        {
            /* Process here text node, It is available in cpStr :TODO: */
            printf("node type: Text, node content: %s,  content length %d\n", (char *)cur_node->content, strlen((char *)cur_node->content));
        }
        traverse_dom_trees(cur_node->children);
    }
}